import typing as t
import json
from flask import Blueprint
import dao
import Account

account_bp = bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('/get-all-accounts')
def get_all_accounts():
    accounts: t.List[account] = dao.get_all_accounts()
    if len(accounts) == 0:
        return json.dumps([])
    else:
        return json.dumps(accounts, default=lambda x: x.__dict__)


@bp.route('/get_account_by_id/<int:id>')
def get_account_by_id(id: int):
    account: Account = dao.get_account_by_id(id)
    if account is None:
        return json.dumps('')
    return json.dumps(account, default=lambda x: x.__dict__)


@bp.route('/get_accounts_by_investor_id/<int:investor_id>')
def get_accounts_by_investor_id(id: int):
    accounts: t.List[account] = dao.get_accounts_by_id(id)
    if len(accounts) == 0:
        return json.dumps([])
    else:
        return json.dumps(accounts, default=lambda x: x.__dict__)


@bp.route('/get-accounts-by-name/<name>')
def get_accounts_by_name(name):
    accounts: t.List[account] = dao.get_accounts_by_name(name)
    if len(accounts) == 0:
        return json.dumps([])
    else:
        return json.dumps(accounts, default=lambda x: x.__dict__)


@ bp.route('/create-account/<account_number>/<investor_id>/<balance>', methods=['POST'])
def create_account(account_number, investor_id, balance):
    account: Account = Account(account_number, investor_id, balance)
    dao.create_account(account_number, investor_id, balance)
    return '', 200


@ bp.route('/update_acct_balance/<investor_id>/<account_balance>', methods=['PUT'])
def update_acct_balance(investor_id, account_balance):
    dao.update_acct_balance(investor_id, account_balance)
    return '', 200


@ bp.route('/delete-account/<id>', methods=['DELETE'])
def delete_account(id):
    dao.delete_account(id)
    return '', 200
