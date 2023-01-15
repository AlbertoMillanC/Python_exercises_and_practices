import json
import boto3

def lambda_handler(event, context):
    # Get the video file from the event
    video_file = event["video"]

    # Instantiate AWS Rekognition client
    rekognition = boto3.client("rekognition")
    # Analize video label,face and object
    labels = rekognition.detect_labels(Video={'S3Object': {'Bucket': video_file["bucket"],'Name': video_file["key"]}})
    faces = rekognition.detect_faces(Video={'S3Object': {'Bucket': video_file["bucket"],'Name': video_file["key"]}})
    objects = rekognition.detect_objects(Video={'S3Object': {'Bucket': video_file["bucket"],'Name': video_file["key"]}})

    # Instantiate AWS MediaConvert client
    mediaconvert = boto3.client("mediaconvert")
    # Get video information
    response = mediaconvert.describe_job(Id=video_file["key"])

    # Prepare metadata for response
    metadata = {
        "fileName": video_file["key"],
        "fileSize": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["segmentLength"],
        "duration": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["segmentLength"],
        "resolution": response["job"]["settings"]["inputs"][0]["videoSelector"]["colorSpace"],
        "videoCodec": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["encryption"]["keyProviderSettings"]["staticKeySettings"]["key"],
        "audioCodec": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["encryption"]["keyProviderSettings"]["staticKeySettings"]["key"],
        "videoBitrate": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["encryption"]["keyProviderSettings"]["staticKeySettings"]["key"],
        "audioBitrate": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["encryption"]["keyProviderSettings"]["staticKeySettings"]["key"],
        "language": response["job"]["settings"]["outputGroupSettings"]["hlsGroupSettings"]["encryption"]["keyProviderSettings"]["staticKeySettings"]["key"],
        "metadata":{
            "faces": [],
            "objects": [],
            "labels": []
        }
    }

    for label in labels["Labels"]:
        metadata["metadata"]["labels"].append({
            "name": label["Name"],
            "confidence": label
            "Confidence"]
for face in faces["FaceDetails"]:
    metadata["metadata"]["faces"].append({
        "name": face["BoundingBox"],
        "confidence": face["Confidence"]
    })
for obj in objects["DetectedObjects"]:
    metadata["metadata"]["objects"].append({
        "name": obj["Name"],
        "confidence": obj["Confidence"]
    })
return {
    "statusCode": 200,
    "body": json.dumps(metadata)
}
                                          
})
        

"""Este ejemplo se basa en la utilización de los servicios AWS Rekognition y AWS MediaConvert para extraer metadatos del video. La función recibiría un evento que contiene la información del archivo de video, y utilizaría esa información para crear clientes de AWS Rekognition y AWS MediaConvert.
La función luego utiliza estos clientes para extraer metadatos del video, como detección de rostros, reconocimiento de objetos y etiquetas, así como información básica del video como la duración, resolución, codecs y tasas de bits.
Finalmente, la función prepara los metadatos extraídos en un archivo JSON y lo devuelve como respuesta a la solicitud. Por favor nota que este ejemplo es solo ilustrativo, y puede que requiera adaptaciones para funcionar en un entorno específico.***
"""

        

