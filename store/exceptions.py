from rest_framework.exceptions import APIException

class InsufficientPointsException(APIException):
    status_code = 400
    default_detail = "포인트가 부족하여 아이템을 구매할 수 없습니다."
    default_code = "insufficient_points"