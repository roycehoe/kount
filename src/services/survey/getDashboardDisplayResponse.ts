import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateTimerResponse } from "./getCreateTimerResponse";


export async function getDashboardDisplayResponse(): Promise<Result<Array<CreateTimerResponse>, ErrorCode>> {
    try {
        const response = await client.get("/timer");
        return Ok(response.data as Array<CreateTimerResponse>)
    }
    catch (error) {
        return Err(getErrorCode(error))
    }
}