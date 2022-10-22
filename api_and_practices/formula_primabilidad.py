import Data.List (sort)
import Data.Numbers.Primes (primes, isPrime)
import I1M.PolOperaciones (valor, consPol, polCero)
import Test.QuickCheck (Positive (Positive), quickCheck)
 
#  1ª solución
#  ===========
 
generadoresMaximales1 :: Integer -> (Int,[(Integer,Integer)])
generadoresMaximales1 n =
  (m,[(a,b) | a <- [-n..n], b <- [-n..n], nPrimos a b == m])
  where m = maximum [nPrimos a b | a <- [-n..n], b <- [-n..n]]
 
 (nPrimos a b) es el número de primos consecutivos generados por el
 polinomio n² + an + b a partir de n=0. Por ejemplo,
    nPrimos (-1) 41     ==  41
    nPrimos (-79) 1601  ==  80
nPrimos :: Integer -> Integer -> Int
nPrimos a b =
  length (takeWhile isPrime [n*n+a*n+b | n <- [0..]])
 
 2ª solución
 ===========
 
 Notas:
 1. Se tiene que b es primo, ya que para n = 0, se tiene que
    0²+a*0+b = b es primo.
 2. Se tiene que 1+a+b es primo, ya que es el valor del polinomio para
    n = 1.
 
generadoresMaximales2 :: Integer -> (Int,[(Integer,Integer)])
generadoresMaximales2 n = (m,map snd zs)
  where xs = [(nPrimos a b,(a,b)) | b <- takeWhile (<=n) primes,
                                    a <- [-n..n],
                                    isPrime(1+a+b)]
        ys = reverse (sort xs)
        m  = fst (head ys)
        zs = takeWhile (\(k,_) -> k == m) ys
 
 3ª solución
 ===========
 
generadoresMaximales3 :: Integer -> (Int,[(Integer,Integer)])
generadoresMaximales3 n = (m,map snd zs)
  where xs = [(nPrimos a b,(a,b)) | b <- takeWhile (<=n) primes,
                                    p <- takeWhile (<=1+2*n) primes,
                                    let a = p-b-1]
        ys = reverse (sort xs)
        m  = fst (head ys)
        zs = takeWhile (\(k,_) -> k == m) ys
 
 4ª solución (con la librería de polinomios)
 ===========================================
 
generadoresMaximales4 :: Integer -> (Int,[(Integer,Integer)])
generadoresMaximales4 n = (m,map snd zs)
  where xs = [(nPrimos2 a b,(a,b)) | b <- takeWhile (<=n) primes,
                                     p <- takeWhile (<=1+2*n) primes,
                                     let a = p-b-1]
        ys = reverse (sort xs)
        m  = fst (head ys)
        zs = takeWhile (\(k,_) -> k == m) ys
 
 (nPrimos2 a b) es el número de primos consecutivos generados por el
 polinomio n² + an + b a partir de n=0. Por ejemplo,
    nPrimos2 (-1) 41     ==  41
    nPrimos2 (-79) 1601  ==  80
nPrimos2 :: Integer -> Integer -> Int
nPrimos2 a b =
  length (takeWhile isPrime [valor p n | n <- [0..]])
  where p = consPol 2 1 (consPol 1 a (consPol 0 b polCero))
 
 Comprobación de equivalencia
 ============================
 
 La propiedad es
prop_generadoresMaximales :: Positive Integer -> Bool
prop_generadoresMaximales (Positive n) =
  all (equivalentes (generadoresMaximales1 n'))
      [generadoresMaximales2 n',
       generadoresMaximales3 n',
       generadoresMaximales4 n']
  where n' = n+1
 
equivalentes :: (Int,[(Integer,Integer)]) -> (Int,[(Integer,Integer)]) -> Bool
equivalentes (n,xs) (m,ys) =
  n == m && sort xs == sort ys
 
 La comprobación es
    λ> quickCheck prop_generadoresMaximales
    +++ OK, passed 100 tests.
 
 Comparación de eficiencia
 =========================
 
 La comparación es
    λ> generadoresMaximales1 300
    (56,[(-31,281)])
    (2.10 secs, 2,744,382,760 bytes)
    λ> generadoresMaximales2 300
    (56,[(-31,281)])
    (0.17 secs, 382,103,656 bytes)
    λ> generadoresMaximales3 300
    (56,[(-31,281)])
    (0.19 secs, 346,725,872 bytes)
    λ> generadoresMaximales4 300
    (56,[(-31,281)])
    (0.20 secs, 388,509,808 bytes)