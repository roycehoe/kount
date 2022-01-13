<script lang="ts" setup>import { ref } from 'vue';

const questionOptions = ref([] as Array<any>)
const questionTitle = ref("")

function addOption() {
  questionOptions.value.push({ option: '' })
}

function removeOption() {
  questionOptions.value.pop()
}

</script>


<template>
  <p>question title{{ questionTitle }}</p>
  <p>question options{{ questionOptions }}</p>
  <input type="text" v-model="questionTitle" />

  <div>
    <div v-for="(questionOption, index) in questionOptions">
      <input v-model="questionOption.option" />
    </div>

    <button @click="addOption" class="bg-slate-400">Add</button>
    <button @click="removeOption" class="bg-slate-400">Remove</button>
  </div>
</template>

<style scoped lang="scss">
</style>