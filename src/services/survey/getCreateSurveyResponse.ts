import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import internal from "stream";


export interface CreateSurveyQuestion {
    title: string
}

export interface CreateSurveyRequest {
    title: string
    questions: Array<CreateSurveyQuestion>
}

interface CreateSurveyResponse {
    user_id: number
    created_at: Float32Array
    name: string
    questions: Array<string>
    id: number
}

export async function getCreateSurveyResponse(createSurveyForm: CreateSurveyRequest): Promise<Result<CreateSurveyResponse, ErrorCode>> {
    try {
        const response = await client.post("/survey", createSurveyForm);
        return Ok(response.data as CreateSurveyResponse)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}