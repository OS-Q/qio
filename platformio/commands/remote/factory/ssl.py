
import certifi
from OpenSSL import SSL  # pylint: disable=import-error
from twisted.internet import ssl  # pylint: disable=import-error


class SSLContextFactory(ssl.ClientContextFactory):
    def __init__(self, host):
        self.host = host
        self.certificate_verified = False

    def getContext(self):
        ctx = super(SSLContextFactory, self).getContext()
        ctx.set_verify(
            SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, self.verifyHostname
        )
        ctx.load_verify_locations(certifi.where())
        return ctx

    def verifyHostname(  # pylint: disable=unused-argument,too-many-arguments
        self, connection, x509, errno, depth, status
    ):
        cn = x509.get_subject().commonName
        if cn.startswith("*"):
            cn = cn[1:]
        if self.host.endswith(cn):
            self.certificate_verified = True
        return status
