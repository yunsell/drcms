from flask import Flask, request, jsonify
from flask_cors import CORS
import mariadb

app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

def get_conn():
    conn = mariadb.connect(
        user="root",
        password="1234",
        host="localhost",
        port=3306,
        database="ai_cms"
    )
    return conn

@app.route('/v1.0/user', methods=['GET'])
def get():
    dictResult: dict = dict()

    # sql = "select email,password,user_name,grade,created_at from user"
    sql = "select * from user where deleted_at"

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        user = cur.fetchall()

        dictResult = [dict(zip([key[0] for key in cur.description], row)) for row in user]

    except Exception as e:
        print(e)

    return jsonify(dictResult)

@app.route('/v1.0/content', methods=['GET'])
def content():
    dictResult: dict = dict()

    sql = "SELECT C.id contentId, C.title, \
                C.content_type contentType, C.clinic, C.clinic_div clinicDiv, \
                C.keyword, C.hospital, C.source, \
                U.user_name registerUserName, \
                C.created_at createdAt, C.updated_at updatedAt \
              FROM content C \
                LEFT JOIN user U \
                  ON C.register_user_id = U.id \
              WHERE C.deleted_at IS NULL \
              ORDER BY C.id DESC"

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        content = cur.fetchall()

        dictResult = [dict(zip([key[0] for key in cur.description], row)) for row in content]

    except Exception as e:
        print(e)

    return jsonify(dictResult)

@app.route('/v1.0/contentnew', methods=['GET'])
def contentnew():
    dictResult: dict = dict()

    sql = "SELECT C.id contentId, \
                C.content_type contentType, C.clinic, C.clinic_div clinicDiv, \
                C.keyword, C.hospital, C.source, \
                P.id paragraphId, P.paragraph_no paragraphNo, P.paragraph_type paragraphType, \
                P.paragraph \
              FROM content C \
                JOIN ( \
                  SELECT P.id, P.content_id, P.paragraph_no, P.paragraph_type, \
                    GROUP_CONCAT(S.sentence ORDER BY S.id) paragraph \
                  FROM paragraph P \
                    JOIN sentence S \
                      ON P.id = S.paragraph_id \
                  GROUP BY P.id, P.content_id, P.paragraph_no, P.paragraph_type \
                ) P \
                  ON C.id = P.content_id \
              WHERE C.deleted_at IS NULL \
              ORDER BY C.id DESC, P.id"

    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sql)
        content = cur.fetchall()

        dictResult = [dict(zip([key[0] for key in cur.description], row)) for row in content]

    except Exception as e:
        print(e)

    return jsonify(dictResult)


if __name__ == "__main__":
    app.run()