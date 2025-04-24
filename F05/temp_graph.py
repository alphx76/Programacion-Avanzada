import re
import pandas as pd
import matplotlib.pyplot as plt

def extract_data_from_log(log_file):
    """
    Extrae los datos relevantes del archivo log.

    Args:
        log_file (str): La ruta al archivo log.

    Returns:
        list: Una lista de listas con los datos extraídos.
    """

    data = []
    with open(log_file, 'r') as f:
        for line in f:
            # Buscar la línea que contiene los datos
            match = re.search(r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\.\d{3}).*M_D=(\d{3}), M_S=(\d{3}), ML_D=(\d{3}), ML_S=(\d{3}), R_D=(\d{3})', line)
            if match:
                timestamp = match.group(1)
                m_d = int(match.group(2))
                m_s = int(match.group(3))
                ml_d = int(match.group(4))
                ml_s = int(match.group(5))
                r_d = int(match.group(6))
                data.append([timestamp, m_d, m_s, ml_d, ml_s, r_d])
    return data

def create_dataframe(data):
    """
    Crea un DataFrame de Pandas a partir de los datos extraídos.

    Args:
        data (list): La lista de datos extraídos.

    Returns:
        pandas.DataFrame: El DataFrame creado.
    """

    df = pd.DataFrame(data, columns=['Timestamp', 'M_D', 'M_S', 'ML_D', 'ML_S', 'R_D'])
    df['Sample'] = range(1, len(df) + 1)  # Añadir la columna 'Sample'
    return df

def plot_data(df):
    """
    Genera los gráficos de las columnas M_D, M_S, ML_D, ML_S y R_D.

    Args:
        df (pandas.DataFrame): El DataFrame con los datos.
    """

    plt.figure(figsize=(12, 10))

    plt.subplot(3, 2, 1)
    plt.plot(df['Sample'], df['M_D'])
    plt.title('M_D over Samples')
    plt.xlabel('Sample')
    plt.ylabel('M_D')

    plt.subplot(3, 2, 2)
    plt.plot(df['Sample'], df['M_S'])
    plt.title('M_S over Samples')
    plt.xlabel('Sample')
    plt.ylabel('M_S')

    plt.subplot(3, 2, 3)
    plt.plot(df['Sample'], df['ML_D'])
    plt.title('ML_D over Samples')
    plt.xlabel('Sample')
    plt.ylabel('ML_D')

    plt.subplot(3, 2, 4)
    plt.plot(df['Sample'], df['ML_S'])
    plt.title('ML_S over Samples')
    plt.xlabel('Sample')
    plt.ylabel('ML_S')

    plt.subplot(3, 2, 5)
    plt.plot(df['Sample'], df['R_D'])
    plt.title('R_D over Samples')
    plt.xlabel('Sample')
    plt.ylabel('R_D')

    plt.tight_layout()
    plt.show()

def save_cleaned_log(df, output_file):
    """
    Guarda los datos limpios en un nuevo archivo log.

    Args:
        df (pandas.DataFrame): El DataFrame con los datos limpios.
        output_file (str): La ruta al archivo de salida.
    """

    with open(output_file, 'w') as f:
        for index, row in df.iterrows():
            log_line = f"{row['Timestamp']} - M_D={row['M_D']}, M_S={row['M_S']}, ML_D={row['ML_D']}, ML_S={row['ML_S']}, R_D={row['R_D']}\n"
            f.write(log_line)

# Uso de las funciones
log_file = 'D:\Cloud\OneDrive\Desktop\XenD103Tool_2025_04_23_10_34_44.log.txt'
data = extract_data_from_log(log_file)
df = create_dataframe(data)
plot_data(df)

output_log_file = 'D:\Cloud\OneDrive\Desktop\cleaned_log.txt'
save_cleaned_log(df, output_log_file)