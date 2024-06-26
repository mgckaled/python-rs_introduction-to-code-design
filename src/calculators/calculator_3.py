from typing import Dict, List

from flask import Request

from src.drivers.interfaces.driver_handler_interface import \
    DriverHandlerInterface
from src.erros.http_bad_request import HttpBadRequestError
from src.erros.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        if variance is None or multiplication is None:
            raise HttpBadRequestError(
                'Valores de variância ou multiplicação são None')

        self.__verify_results(variance, multiplication)
        formated_response = self.__format_response(variance)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num

        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance is None or multiplication is None:
            raise HttpBadRequestError(
                'Valores de entrada são None, não é possível comparar')
        if not isinstance(variance, (int, float)) or not isinstance(multiplication, (int, float)):
            raise HttpBadRequestError(
                'Valores de entrada não são numéricos')
        if variance < multiplication:
            raise HttpBadRequestError(
                'Falha no processo: Variância menor que multiplicação')

    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True,
            }
        }
