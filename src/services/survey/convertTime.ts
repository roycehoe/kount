
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