<script lang="ts" setup>
import { ref } from "vue";
import router from "@/router";
import { ErrorCode, ErrorMsg } from "@/services/errors";
import { AuthUserRequest, AuthUserResponse, getAuthUserResponse } from "@/services/user/getAuthUserResponse";
import { client } from "@/services";

async function helloWorld() {
  return await client.post("https://jsonplaceholder.typicode.com/todos/1")
}

</script>

<template>
  <p class="hello-world">{{ helloWorld() }}</p>
</template>

<style scoped lang="scss">
.hello-world {
  background-color: black;
  color: white;
}
</style>