from graphene.types import Scalar
from graphql.language import ast
from graphql import GraphQLError
import re


class CNPJ(Scalar):
    """CNPJ Scalar Description"""

    ERROR_MESSAGE = "Invalid document number"

    @classmethod
    def serialize(cls, value):
        return value

    @classmethod
    def valid_cnpj(cls, value):
        # https://wiki.python.org.br/VerificadorDeCpfCnpjSimples

        cnpj = "".join(re.findall(r"\d", str(value)))

        invalid_cnpjs = []
        for x in range(10):
            invalid_cnpjs.append("".join(str(x) for y in range(15)))

        if (not cnpj) or (len(cnpj) < 14) or cnpj in invalid_cnpjs:
            raise GraphQLError(cls.ERROR_MESSAGE)

        integers = list(map(int, cnpj))
        new = integers[:12]

        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        while len(new) < 14:
            r = sum([x * y for (x, y) in zip(new, prod)]) % 11
            if r > 1:
                f = 11 - r
            else:
                f = 0
            new.append(f)
            prod.insert(0, 6)

        if new == integers:
            return value

        raise GraphQLError(cls.ERROR_MESSAGE)

    @classmethod
    def parse_literal(cls, node):
        if isinstance(node, ast.StringValue) and cls.valid_cnpj(node.value):
            return node.value
        else:
            raise GraphQLError(cls.ERROR_MESSAGE)

    @classmethod
    def parse_value(cls, value):
        if cls.valid_cnpj(value):
            return value
        else:
            raise GraphQLError(cls.ERROR_MESSAGE)
