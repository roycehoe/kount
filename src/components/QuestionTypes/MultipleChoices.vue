<script lang="ts" setup>
</script>

<template>
    <div class="form-control">
        <label class="label">
            <span class="label-text font-bold">Question</span>
        </label>
        <input type="text" placeholder="Name" class="input input-bordered" />
    </div>
    <div class="p-6 card bordered">
        <div class="form-control">
            <label class="label">
                <input
                    type="text"
                    placeholder="Choice..."
                    class="input input-bordered w-full mr-20"
                />
                <button>
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        class="h-6 w-6 hover:bg-slate-100"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="{2}"
                            d="M18 12H6"
                        />
                    </svg>
                </button>
            </label>

            <button class="hover:bg-neutral-100 flex flex-row my-5">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="{2}"
                        d="M12 4v16m8-8H4"
                    />
                </svg>
                <p>Add Option</p>
            </button>
        </div>
    </div>
</template>
<style scoped lang="scss">
</style>