import boto3
from botocore.exceptions import ClientError, NoCredentialsError

try:
    # Inicializar el cliente de EC2 en tu región
    ec2 = boto3.client('ec2', region_name='us-east-2')

    # Consultar instancias (pueden estar running, stopped, etc.)
    response = ec2.describe_instances()

    print("Conexión exitosa. Instancias encontradas:")
    for reservation in response.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            instance_id = instance.get('InstanceId')
            state = instance.get('State', {}).get('Name')
            ip_publica = instance.get('PublicIpAddress', 'Sin IP')
            print(f"ID: {instance_id} | Estado: {state} | IP pública: {ip_publica}")

    if not response.get('Reservations'):
        print("No hay instancias en esta región.")

except NoCredentialsError:
    print("No hay credenciales de AWS configuradas. Ejecuta 'aws configure' o 'aws sso login'.")
except ClientError as e:
    print(f"Error de AWS: {e}")
    print("Revisa permisos IAM y que tu usuario tenga ec2:DescribeInstances.")
