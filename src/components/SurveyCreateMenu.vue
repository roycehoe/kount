<script lang="ts" setup>
import { ref } from 'vue';
import PlusIcon from './Icons/PlusIcon.vue';
import MinusIcon from './Icons/MinusIcon.vue';
import internal from 'stream';

interface getCreateTimerResponse {
    title: string
    hours: number
    minutes: number
    seconds: number
}



const isCreateTimer = ref(false)
const createTimerForm = ref({} as getCreateTimerResponse)




</script>

<template>
    <p>{{ createTimerForm }}</p>
    <button class="hover:bg-neutral-100 flex flex-row" @click="isCreateTimer = !isCreateTimer">
        <MinusIcon class="mb-2" v-if="isCreateTimer"></MinusIcon>
        <div class="flex" v-else>
            <PlusIcon></PlusIcon>
            <p class="ml-2">New timer</p>
        </div>
    </button>

    <div v-if="isCreateTimer">
        <div class="form-control">
            <input
                type="text"
                placeholder="Name"
                class="input input-bordered"
                v-model="createTimerForm.title"
            />
        </div>
        <div class="divider"></div>

        <div class="timer-form flex">
            <div class="timer-form--inputs">
                <input type="range" max="24" class="range" v-model="createTimerForm.hours" />
                <input type="range" max="60" class="range" v-model="createTimerForm.minutes" />
                <input type="range" max="60" class="range" v-model="createTimerForm.seconds" />
                <!-- note to self - set default value  -->
            </div>
            <div class="timer-form--display">
                <div class="w-full shadow stats">
                    <div class="stat">
                        <div class="stat-figure text-secondary">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                class="inline-block w-8 h-8 stroke-current"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                />
                            </svg>
                        </div>
                        <div class="stat-title">Downloads</div>
                        <div class="stat-value">310M</div>
                        <div class="stat-desc">Jan 1st - Feb 1st</div>
                    </div>
                    <div class="stat">
                        <div class="stat-figure text-secondary">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                class="inline-block w-8 h-8 stroke-current"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"
                                />
                            </svg>
                        </div>
                        <div class="stat-title">New Users</div>
                        <div class="stat-value">4,200</div>
                        <div class="stat-desc text-success">↗︎ 400 (22%)</div>
                    </div>
                    <div class="stat">
                        <div class="stat-figure text-secondary">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                                class="inline-block w-8 h-8 stroke-current"
                            >
                                <path
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    stroke-width="2"
                                    d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"
                                />
                            </svg>
                        </div>
                        <div class="stat-title">New Registers</div>
                        <div class="stat-value">1,200</div>
                        <div class="stat-desc text-error">↘︎ 90 (14%)</div>
                    </div>
                </div>
                <p>HOURS</p>
                <p>MINUTES</p>
                <p>SECONDS</p>
            </div>
        </div>

        <div class="divider"></div>

        <div>
            <button
                class="bg-green-500 mw-2 w-full h-10 rounded-md hover:bg-green-600 my-3"
            >Create Timer</button>
        </div>
        <div>
            <button
                class="bg-red-500 mw-2 w-full h-10 rounded-md hover:bg-red-600 my-3"
                @click="isCreateTimer = false"
            >Exit</button>
        </div>
    </div>
</template>

<style scoped lang="scss">
</style>