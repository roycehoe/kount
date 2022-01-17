interface MetricTime {
    hours: number
    minutes: number
    seconds: number
}

export interface TimerDisplay {
    id: number
    title: string
    createdAt: any
    hours: number
    minutes: number
    seconds: number
    time: number
}

export interface CreateTimerDisplay {
    title: string
    hours: number
    minutes: number
    seconds: number
}


export function getMetricTime(seconds: number): MetricTime {
    return {
        hours: Math.floor(seconds / 3600) % 24,
        minutes: Math.floor(seconds / 60) % 60,
        seconds: Math.floor(seconds) % 60
    }
}

function getSecondsPlaceholder(metricTime: MetricTime): number {
    return ((metricTime.hours * 60 * 60) + (metricTime.minutes * 60) + metricTime.seconds)
}