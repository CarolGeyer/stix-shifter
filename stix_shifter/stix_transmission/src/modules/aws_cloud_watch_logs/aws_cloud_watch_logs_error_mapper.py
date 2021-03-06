from .....utils.error_mapper_base import ErrorMapperBase
from .....utils.error_response import ErrorCode

ERROR_MAPPING = {
    "InvalidParameterException": ErrorCode.TRANSMISSION_INVALID_PARAMETER,
    "ParamValidationError": ErrorCode.TRANSMISSION_INVALID_PARAMETER,
    "UnknownOperationException": ErrorCode.TRANSMISSION_INVALID_PARAMETER,
    "UnrecognizedClientException": ErrorCode.TRANSMISSION_AUTH_CREDENTIALS,
    "ClientError": ErrorCode.TRANSMISSION_AUTH_CREDENTIALS,
    "InvalidSignatureException": ErrorCode.TRANSMISSION_AUTH_CREDENTIALS,
    "SerializationException": ErrorCode.TRANSMISSION_QUERY_PARSING_ERROR,
    "ServiceUnavailableException": ErrorCode.TRANSMISSION_CONNECT,
    "LimitExceededException": ErrorCode.TRANSMISSION_SEARCH_DOES_NOT_EXISTS,
    "MalformedQueryException": ErrorCode.TRANSMISSION_QUERY_PARSING_ERROR,
    "ResourceNotFoundException": ErrorCode.TRANSMISSION_SEARCH_DOES_NOT_EXISTS,
    "JSONDecodeError": ErrorCode.TRANSMISSION_QUERY_PARSING_ERROR,
    "EndpointConnectionError": ErrorCode.TRANSMISSION_CONNECT,
    "ConnectTimeoutError": ErrorCode.TRANSMISSION_CONNECT
    }


class ErrorMapper:
    """"ErrorMapper class"""
    DEFAULT_ERROR = ErrorCode.TRANSMISSION_MODULE_DEFAULT_ERROR

    @staticmethod
    def set_error_code(json_data, return_obj):
        """aws transmit specified error
         :param json_data: dict, error response of api_call
         :param return_obj: dict, returns error and error code"""
        error_type = ''
        try:
            error_type = json_data['__type']
        except KeyError:
            pass

        error_code = ErrorMapper.DEFAULT_ERROR

        if error_type in ERROR_MAPPING:
            error_code = ERROR_MAPPING[error_type]

        if error_code == ErrorMapper.DEFAULT_ERROR:
            print("failed to map: " + str(json_data))

        ErrorMapperBase.set_error_code(return_obj, error_code)
