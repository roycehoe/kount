<script lang="ts" setup>
import { ref } from 'vue';
import PlusIcon from './Icons/PlusIcon.vue';
import MinusIcon from './Icons/MinusIcon.vue';
import { CreateTimerDisplay } from '@/services/timer/convertTime';
import { CreateTimerRequest, getCreateTimerResponse } from '@/services/timer/getCreateTimerResponse';


const DEFAULT_CREATE_TIMER_FORM_DISPLAY = {
  title: "",
  hours: 0,
  minutes: 5,
  seconds: 0
}
const isCreateTimer = ref(false)
const createTimerFormDisplay = ref(DEFAULT_CREATE_TIMER_FORM_DISPLAY as CreateTimerDisplay)

function getCreateTimerSeconds(): number {
  const convertedHours = createTimerFormDisplay.value.hours * 60 * 60
  const convertedMinutes = createTimerFormDisplay.value.minutes * 60

  return (convertedHours + convertedMinutes + createTimerFormDisplay.value.seconds)
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
  <div class="divider"></div>

  <div v-if="isCreateTimer">
    <div class="form-control">
      <input
        type="text"
        placeholder="Timer name"
        maxlength="50"
        class="input input-info input-bordered"
        v-model="createTimerFormDisplay.title"
      />
    </div>
    <div class="divider"></div>

    <div class="timer-form flex justify-between">
      <div class="timer-form--selection flex">
        <div class="timer-form--inputs">
          <input type="range" max="24" class="range" v-model.number="createTimerFormDisplay.hours" />
          <input
            type="range"
            max="59"
            class="range"
            v-model.number="createTimerFormDisplay.minutes"
          />
          <input
            type="range"
            max="59"
            class="range"
            v-model.number="createTimerFormDisplay.seconds"
          />
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
          :class="{ 'btn-disabled bg-slate-400': !getCreateTimerSeconds() }"
        >Create Timer</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>