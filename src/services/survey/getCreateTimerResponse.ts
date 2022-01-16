import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";



export interface CreateTimerRequest {
    title: string
    time: number
}

export interface CreateTimerResponse {
    id: number
    created_at: any //to ammend
    title: string
    time: number
}

export async function getCreateSurveyResponse(createTimerForm: CreateTimerRequest): Promise<Result<CreateTimerResponse, ErrorCode>> {
    try {
        const response = await client.post("/timer", createTimerForm);
        return Ok(response.data as CreateTimerResponse)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}