import csv
import io
from models import Receita

class ExportadorCSV:
    
    @staticmethod
    def gerar_csv(dados_banco):
        """
        Transforma os dados brutos do banco num fluxo de bytes (ficheiro em memória).
        """

        output = io.StringIO()
        writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(['ID', 'Valor', 'Categoria', 'Descrição', 'Tipo', 'Data'])

        for item in dados_banco:
            writer.writerow(item)

        output.seek(0)
        return io.BytesIO(output.getvalue().encode('utf-8'))