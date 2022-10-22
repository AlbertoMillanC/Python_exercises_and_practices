# From documentation

# Create data
d <- diamonds[sample(nrow(diamonds), 1000), ]

# Create plot, specifying hover text
p <- plot_ly(
  d, x = ~carat, y = ~price, mode = "markers", type = "scatter",
  # Hover text:
  text = ~paste0("Price:$", price, '<br>Cut: ', cut),
  color = ~carat, size = ~carat
)

# Show chart
p