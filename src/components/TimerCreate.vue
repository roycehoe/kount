<script lang="ts" setup>
import { ref } from 'vue';
import PlusIcon from './Icons/PlusIcon.vue';
import MinusIcon from './Icons/MinusIcon.vue';
import { getSeconds } from '@/services/survey/convertTime';
import { client } from '@/services';
import { CreateTimerRequest, getCreateTimerResponse } from '@/services/survey/getCreateTimerResponse';


const DEFAULT_CREATE_TIMER_FORM_DISPLAY = {
  title: "",
  hours: 0,
  minutes: 15,
  seconds: 0
}

interface CreateTimerDisplay {
  title: string
  hours: number
  minutes: number
  seconds: number
}

const isCreateTimer = ref(false)
const createTimerFormDisplay = ref(DEFAULT_CREATE_TIMER_FORM_DISPLAY as CreateTimerDisplay)

function getCreateTimerSeconds() {
  return getSeconds(createTimerFormDisplay.value.hours, createTimerFormDisplay.value.minutes, createTimerFormDisplay.value.seconds)
  //please refactor this
}

async function createTimer() {
  const { ok: isSuccessful, val: response } = await getCreateTimerResponse({ title: createTimerFormDisplay.value.title, time: getCreateTimerSeconds() } as CreateTimerRequest)
  if (isSuccessful) {
    location.reload()
    return
  }
  console.log(response)
}


</script>

<template>
  <button class="hover:bg-neutral-100 flex flex-row" @click="isCreateTimer = !isCreateTimer">
    <div class="flex">
      <MinusIcon class="mb-2" v-if="isCreateTimer"></MinusIcon>
      <PlusIcon class="mb-2" v-else></PlusIcon>
      <p class="ml-2">Create a new timer</p>
    </div>
  </button>

  <div v-if="isCreateTimer">
    <div class="form-control">
      <input
        type="text"
        placeholder="Timer name"
        class="input input-bordered"
        v-model="createTimerFormDisplay.title"
      />
    </div>
    <div class="divider"></div>

    <div class="timer-form flex justify-between">
      <div class="timer-form--selection flex">
        <div class="timer-form--inputs">
          <input type="range" max="23" class="range" v-model="createTimerFormDisplay.hours" />
          <input type="range" max="59" class="range" v-model="createTimerFormDisplay.minutes" />
          <input type="range" max="59" class="range" v-model="createTimerFormDisplay.seconds" />
          <!-- note to self - set default value  -->
        </div>

        <div class="timer-form--display grid grid-flow-col gap-5 text-center auto-cols-max ml-10">
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerFormDisplay.hours }}</p>
            <p>hours</p>
          </div>
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerFormDisplay.minutes }}</p>
            <p>minutes</p>
          </div>
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerFormDisplay.seconds }}</p>
            <p>seconds</p>
          </div>
        </div>
      </div>
      <div class="timer-form--buttons flex items-center">
        <button
          @click="createTimer"
          class="btn btn-success bg-green-500 border-none hover:bg-green-600"
          :class="{ 'btn-disabled bg-slate-400': !createTimerFormDisplay.title || !getCreateTimerSeconds() }"
        >Create Timer</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>