import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateSurveyResponse } from "./getCreateSurveyResponse";

export interface GetDeleteSurveyRequest {
    survey_id: number
}

export interface something {
    survey_id: number
}


export async function getDeleteSurveyResponse(deleteSurveyRequest: GetDeleteSurveyRequest): Promise<Result<void, ErrorCode>> {
    try {
        const response = await client.delete("/survey", { data: deleteSurveyRequest });
        return Ok(response.data as void)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}