import { Ok, Err, Result } from "ts-results"
import { client } from "@/services"
import { ErrorCode, getErrorCode } from "@/services/errors";
import { CreateTimerResponse } from "./getCreateTimerResponse";

export interface DeleteTimerRequest {
    timer_id: number
}


export async function getDeleteTimerResponse(deleteTimerForm: DeleteTimerRequest): Promise<Result<void, ErrorCode>> {
    try {
        const response = await client.delete("/timer", { data: deleteTimerForm });
        return Ok(response.data as void)
    }
    catch (error) {
        console.log('got error')
        return Err(getErrorCode(error))
    }
}