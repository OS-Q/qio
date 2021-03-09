
import jsonrpc

from core.clients.account import AccountClient


class AccountRPC:
    @staticmethod
    def call_client(method, *args, **kwargs):
        try:
            client = AccountClient()
            return getattr(client, method)(*args, **kwargs)
        except Exception as e:  # pylint: disable=bare-except
            raise jsonrpc.exceptions.JSONRPCDispatchException(
                code=4003, message="PIO Account Call Error", data=str(e)
            )
