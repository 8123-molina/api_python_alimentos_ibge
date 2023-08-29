import mysql.connector
from flask import Flask, jsonify, request

mydb = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='',
    database='db_alimentos'
)
app = Flask(__name__)
my_cursor = mydb.cursor()


# Tets de conexao da API
@app.route('/api/v1/', methods=['GET'])
def teste_conexao():
    return jsonify(
        mensagem='Api encontra-se online para verificar a documentação acesse /doc',
        
    )

# Tets de conexao da API
@app.route('/api/v1/doc', methods=['GET'])
def docuemntacao():
    return jsonify(
        mensagem='Aqui ficara a view de documentação',
        
    )


# Consultar por descrição alimento
@app.route('/api/v1/alimentos/pesquisar/<string:text>', methods=['GET'])
def pesquisar_alimentos(text):
    sql = f"SELECT * FROM ibge_alimentos where descricao LIKE ('%{text}%')"
    my_cursor.execute(sql)
    res_alimentos = my_cursor.fetchall()

    alimentos = list()
    for alimento in res_alimentos:
        print(alimento[3])
        alimentos.append(
            {
                'id': alimento[0],
	            'cd_ibge': alimento[1],
                'descricao': alimento[2],
	            'cd_md_preparo': alimento[3],
	            'energia_kcal': alimento[4],
	            'proteina_g': alimento[5],
	            'lipidios_totais_g': alimento[6],
	            'carboidrato_g': alimento[7],
	            'fibra_alimentar_total_g': alimento[8],
	            'calcio_mg': alimento[9],
	            'magnesio_mg': alimento[10],
	            'manganes_mg': alimento[11],
	            'foforo_mg': alimento[12],
	            'ferro_mg': alimento[13],
	            'sodio_mg': alimento[14],
	            'sodio_adicao_mg': alimento[15],
	            'potassio_mg': alimento[16],
	            'cobre_mg': alimento[17],
	            'zinco_mg': alimento[18],
	            'selenio_mcg': alimento[19],
	            'colesterol_mg': alimento[20],
	            'ag_saturados_g': alimento[21],
	            'ag_mono_g': alimento[22],
	            'ag_poli_g': alimento[23],
	            'ag_linoleico_g': alimento[24],
	            'ag_linolenico_g': alimento[25],
	            'ag_transtotal_g': alimento[26],
	            'acucar_total_g': alimento[27],
	            'acucar_adicao_g': alimento[28],
	            'retinol_mcg': alimento[29],
	            'vitamina_a_rae_mcg': alimento[30],
	            'tiamina_mg': alimento[31],
	            'riboflavina_mg': alimento[32],
	            'niacina_mg': alimento[33],
	            'niacina_ne_mg': alimento[34],
	            'piridoxina_mg': alimento[35],
	            'cabolamina_mcg': alimento[36],
	            'folato_dfe_mcg': alimento[37],
	            'vitamina_d_mg': alimento[38],
	            'vitamina_e_mg': alimento[39],
	            'vitamina_c_mg': alimento[40],
	            'created_at': alimento[41],
	            'updated_at': alimento[42],
            }
        )
    itens = len(alimentos)
    return jsonify(
        mensagem='Sua pesquisa retornou '+str(itens)+' para o texto: ('+text+')',
        dados=alimentos

    )


# Consultar alimeto(id)
@app.route('/api/v1/alimentos/<int:id>', methods=['GET'])
def obter_alimento_to_id(id):
    sql = f"SELECT * FROM ibge_alimentos where descricao LIKE ('%{id}%')"
    my_cursor.execute(sql)
    res_alimentos = my_cursor.fetchall()

    return jsonify(res_alimentos)


# Consultar modo preparo (id)
@app.route('/api/v1/alimentos/<int:id>', methods=['GET'])
def obter_modo_preparo_id(id):
    sql = f"SELECT * FROM ibge_alimentos where descricao LIKE ('%{id}%')"
    my_cursor.execute(sql)
    res_alimentos = my_cursor.fetchall()

    return jsonify(res_alimentos)


# Consultar modo de preparo alimento por (id)
@app.route('/api/v1/alimentos/modo-preparo/<int:id>', methods=['PUT'])
def editar_alimento_to_id(id):
    alimento_alterado = request.get_json()
    for indice,alimento in enumerate(alimentos):
        if alimento.get('id') == id:
            alimentos[indice].update(alimento_alterado)
            return jsonify( "alimento encontrado:",alimentos[indice], "Será alterado para :", alimentos[indice])

# Incluir novo alimento
@app.route('/api/v1/alimentos', methods=['POST'])
def incluir_novo_alimento():
    novo_alimento = request.get_json()
    alimentos.append(novo_alimento)

    return jsonify(alimentos)

# Excluir alimento (id)
@app.route('/api/v1/alimentos/<int:id>', methods=['DELETE'])
def excluir_alimento(id):
    for indice,alimento in enumerate(alimentos):
        if alimento.get('id') == id:
            del alimentos[indice]

    return jsonify(alimentos)


app.run(port=3001,host='localhost',debug=True)