import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateSurveyResponse } from "./getCreateSurveyResponse";


export async function getSurveyQuestions(survey_id: number): Promise<Result<CreateSurveyResponse, ErrorCode>> {
    try {
        const response = await client.get(`/survey/submit/${survey_id}`);
        return Ok(response.data as CreateSurveyResponse)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}