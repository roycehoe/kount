<script lang="ts" setup>import { getDashboardDisplayResponse, GetDashboardDisplayResponse } from '@/services/survey/getDashboardDisplayResponse';
import { onBeforeMount, ref } from 'vue';


const surveyLink = ref("another")
const dashboardInfo = ref({} as GetDashboardDisplayResponse)


async function copyToClipboard(text: string) {
    await navigator.clipboard.writeText(text);
    alert('Link coppied');
}

async function showDashboardInfo() {
    const { ok: isSuccessful, val: response } = await getDashboardDisplayResponse()
    if (isSuccessful) {
        dashboardInfo.value = response as GetDashboardDisplayResponse
    }
    // to implement error handling
}



onBeforeMount(async () => await showDashboardInfo());

</script>


<template>
    <p>{{ dashboardInfo }}</p>
    <div v-for="surveys in dashboardInfo">
        <div class="survey bg-neutral-100 rounded-md flex flex-row justify-between m-2 bg-gray-50">
            <div class="flex items-center">
                <p class="m-3">{{ surveys.title }}</p>
                <button class="m-2" @click="copyToClipboard(surveyLink)">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-5 w-5 text-gray-500"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                    >
                        <path
                            fill-rule="evenodd"
                            d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z"
                            clip-rule="evenodd"
                        />
                    </svg>
                </button>
            </div>

            <div class="flex items-center">
                <button class="bg-green-500 m-2 w-16 h-8 rounded-md hover:bg-green-600">View</button>
                <button class="bg-red-500 m-2 w-16 h-8 rounded-md hover:bg-red-600">Delete</button>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
</style>