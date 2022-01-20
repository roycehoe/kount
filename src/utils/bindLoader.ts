import { Ref } from 'vue'

export function createLoadingFunction<
    CallbackArgs extends any[],
    CallbackReturnValue
>(
    callback: (...args: CallbackArgs) => CallbackReturnValue,
    isLoading: Ref<boolean>
) {
    return async (...args: CallbackArgs): Promise<CallbackReturnValue> => {
        isLoading.value = true
        const result = callback(...args)
        isLoading.value = false
        return result
    }
}
