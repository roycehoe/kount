<script lang="ts" setup>
import { ref } from 'vue';
import PlusIcon from './Icons/PlusIcon.vue';
import MinusIcon from './Icons/MinusIcon.vue';
import internal from 'stream';


const DEFAULT_CREATE_TIMER_FORM = {
  title: "",
  hours: 0,
  minutes: 15,
  seconds: 0
}

interface getCreateTimerResponse {
  title: string
  hours: number
  minutes: number
  seconds: number
}

const isCreateTimer = ref(false)
const createTimerForm = ref(DEFAULT_CREATE_TIMER_FORM as getCreateTimerResponse)

const test = 10 as number



</script>

<template>
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
        placeholder="Timer name"
        class="input input-bordered"
        v-model="createTimerForm.title"
      />
    </div>
    <div class="divider"></div>

    <div class="timer-form flex justify-between">
      <div class="timer-form--selection flex">
        <div class="timer-form--inputs">
          <input type="range" max="24" class="range" v-model="createTimerForm.hours" />
          <input type="range" max="60" class="range" v-model="createTimerForm.minutes" />
          <input type="range" max="60" class="range" v-model="createTimerForm.seconds" />
          <!-- note to self - set default value  -->
        </div>

        <div class="timer-form--display grid grid-flow-col gap-5 text-center auto-cols-max ml-10">
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerForm.hours }}</p>
            <p>hours</p>
          </div>
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerForm.minutes }}</p>
            <p>minutes</p>
          </div>
          <div class="flex flex-col">
            <p class="font-mono text-5xl">{{ createTimerForm.seconds }}</p>
            <p>seconds</p>
          </div>
        </div>
      </div>
      <div class="timer-form--buttons flex items-center">
        <button class="btn btn-success bg-green-500 border-none hover:bg-green-600">Create Timer</button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
</style>