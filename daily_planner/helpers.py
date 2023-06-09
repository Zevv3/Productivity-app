from functools import wraps
from flask import json
import decimal

# def token_required(our_flask_function):
#     @wraps(our_flask_function)
#     def decorated(*args, **kwargs):
#         token = None

#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token'].split()[1]
#             print(token)
#         if not token:
#             return jsonify({'message': 'Token is Missing!'}), 401
#         try:
#             current_user_token = User.query.filter_by(token = token).first()
#             print(current_user_token)
#             if not current_user_token or current_user_token.token != token:
#                 return jsonify({'message': 'Token is invalid!'})
#         except:
#             owner = User.query.filter_by(token=token).first()
#             if token != owner.token and secrets.compare_digest(token, owner.token):
#                 return jsonify({'message': 'Invalid Token!'})
#         return our_flask_function(current_user_token, *args, **kwargs)
#     return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)