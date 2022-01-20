import { AxiosError } from "axios"
import request from "axios"

export interface ErrorDetail {
    detail: detail
}

interface detail {
    msgs: Array<msg>
    error: ErrorCode
}

interface msg {
    loc: Array<string>
    msg: string
    type: string
}

export enum ErrorCode {
    USER_NOT_FOUND = "USER_NOT_FOUND",
    TOKEN_AUTHENTICATION_FAILED = "TOKEN_AUTHENTICATION_FAILED",
    USERNAME_TAKEN = "USERNAME_TAKEN",
    INVALID_CREDENTIALS = "INVALID_CREDENTIALS",
    REQUEST_MAXIMUM_LENGTH_EXCEEDED = "REQUEST_MAXIMUM_LENGTH_EXCEEDED",
    UNKNOWN_ERROR_OCCURRED = "UNKNOWN_ERROR_OCCURRED",
    TYPE_VALIDATION_ERROR = "TYPE_VALIDATION_ERROR",
    MISSING_AUTHENTICATION_TOKEN = "MISSING_AUTHENTICATION_TOKEN",
    MISSING_FIELD_VALUES = "MISSING_FIELD_VALUES",
    MALFORMED_REQUEST_ERROR = "MALFORMED_REQUEST_ERROR",
}

export enum ErrorMsg {
    NO_ERROR_MSG = "",
    INVALID_CREDENTIALS = "Invalid credentials",
    MISSING_LOGIN_FIELDS = "Please enter your username and password",
    SOMETHING_WENT_WRONG = "Something went wrong",
    FORM_NOT_FILLED = "Form not filled",
    USERNAME_TOO_LONG = "Username must not exceed 20 characters",
    NON_MATCHING_PASSWORDS = "Password must match confirmed password",
    USERNAME_TAKEN = "Username taken. Please try again"
}

export function getErrorCode(error: AxiosError | unknown): ErrorCode {
    if (request.isAxiosError(error)) {
        return error.response?.data.detail.error as ErrorCode
    }
    return ErrorCode.UNKNOWN_ERROR_OCCURRED as ErrorCode
}
