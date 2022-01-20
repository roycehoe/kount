import { getDashboardInfoResponse } from "@/services/timer/getDashboardDisplayResponse"
import { CreateTimerResponse } from "@/services/timer/getCreateTimerResponse"
import { ErrorCode } from "@/services/errors"
import { getMetricTime, TimerDisplay } from "@/services/timer/convertTime"
import { createLoadingFunction } from '@/utils/bindLoader'
import { ref } from 'vue'

let activeTimer = {} as TimerDisplay

export function useTimers() {

    const isGetAllTimersLoading = ref(false)
    const getAllTimers = createLoadingFunction(_getAllTimers, isGetAllTimersLoading)

    async function _getAllTimers() {
        const { ok: isSuccessful, val: response } = await getDashboardInfoResponse()

        if (isSuccessful) {
            return _createTimerArray(response)
        }
        return response as ErrorCode
    }

    function decrementActiveTimer() {
        activeTimer = activeTimer - 1;
    }

    function _createTimerArray(timerResponse) {
        const timerArray = [] as Array<TimerDisplay>

        timerResponse.forEach(timer => {
            timerArray.push({
                id: timer.id,
                title: timer.title,
                createdAt: timer.created_at,
                hours: getMetricTime(timer.time).hours,
                minutes: getMetricTime(timer.time).minutes,
                seconds: getMetricTime(timer.time).seconds,
                time: timer.time
            })
        })

        return timerArray
    }

    function setActiveTimer(selectedTimer: TimerDisplay) {
        activeTimer = selectedTimer
    }

    function getActiveTimer() {
        return activeTimer
    }

    return { isGetAllTimersLoading, getAllTimers, setActiveTimer, getActiveTimer }
}