interface MetricTime {
    hours: number
    minutes: number
    seconds: number
}



export function showHours(seconds: number) {
    return Math.floor(seconds / 3600) % 24
}

export function showMinutes(seconds: number) {
    return Math.floor(seconds / 60) % 60
}

export function showSeconds(seconds: number) {
    return Math.floor(seconds) % 60
}

export function getSeconds(hours: number, minutes: number, seconds: number) {
    return ((hours * 60 * 60) + (minutes * 60) + seconds)
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