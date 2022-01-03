<script lang="ts" setup>
import { getAssetUrl } from '@/services/assets';

function hello() {
  return "hello"
}

</script>

<template>
  <div class="display">
    <div class="display--flexboxColumn display--onGrid">
      <div class="logo">
        <img class="logo--smallImg" src="../assets/graphics/logo.png" />
      </div>

      <div class="display--inputBox">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.logo {
  display: flex;
  justify-content: center;
  margin-bottom: 5vh;
  &--smallImg {
    width: 200px;
  }
}

.display {
  margin: auto;
  width: 20%;
  margin-top: 10vh;
  padding: 10px;
}
</style>