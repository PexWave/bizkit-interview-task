from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    users = []
    if args:
        for user in USERS:
            
            if args.get('age'):
                for key, value in user.items():
                    if value in range(int(args.get('age')) - 1, int(args.get('age')) + 2):
                        users.append(user)

            if args.get('id'):
                if args.get('id') in user.get('id') and user.get("id") not in [user.get('id') for user in users]:
                    users.append(user)

            if args.get('name'):
                if args.get('name') in user.get('name') and user.get("id") not in [user.get('id') for user in users]:
                    users.append(user)
            
            if args.get('occupation') and user.get("id") not in [user.get('id') for user in users]:
                if args.get('occupation') in user.get('occupation'):
                    users.append(user)
        return users

    return USERS
