<template>
    <q-layout view="lHh lpR fFf">

        <q-header elevated class="bg-primary text-white" height-hint="98">
            <q-toolbar>
                <q-btn dense flat round icon="menu" @click="left = !left"/>

                <q-toolbar-title>
                    <q-avatar>
                        <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
                    </q-avatar>
                    Title
                </q-toolbar-title>
            </q-toolbar>

            <q-tabs align="left">
                <q-route-tab to="/page1" label="Page One"/>
                <q-route-tab to="/page2" label="Page Two"/>
                <q-route-tab to="/page3" label="Page Three"/>
            </q-tabs>
        </q-header>

        <q-drawer v-model="left" side="left" overlay behavior="mobile" bordered>
            <!-- drawer content -->
        </q-drawer>

        <q-page-container>
            <Personaggio/>
        </q-page-container>

    </q-layout>
</template>

<script>
    import Personaggio from './components/Personaggio'
    export default {
        components: {Personaggio},
        data() {
            return {
                left: false,
                counter: 0
            }
        },
        methods: {
            startCounting() {
                this.timer = setInterval(() => {
                    this.counter++
                }, 1000)
            },

            stopCounting() {
                clearInterval(this.timer)
            }
        },
        beforeDestroy() {
            this.stopCounting()
        }
    }
</script>