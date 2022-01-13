import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateSurveyResponse } from "./getCreateSurveyResponse";

export interface GetDashboardDisplayResponse {
    dashboardDisplay: Array<CreateSurveyResponse>
}


export async function getDashboardDisplayResponse(): Promise<Result<GetDashboardDisplayResponse, ErrorCode>> {
    try {
        const response = await client.get("/survey");
        return Ok(response.data as GetDashboardDisplayResponse)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}