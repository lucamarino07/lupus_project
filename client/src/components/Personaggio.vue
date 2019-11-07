<template>
    <!--    <q-page class="flex flex-center">-->
    <div class="q-pa-md">
        <q-expansion-item
                class="shadow-1 overflow-hidden q-mb-lg"
                style="border-radius: 30px"
                icon="explore"
                :label="personaggio.nome"
                header-class="bg-primary text-white"
                expand-icon-class="text-white"
                v-for="(personaggio, index) in personaggi" :key="index"
        >
            <q-card>
                <q-card-section>
                    <p>{{personaggio.descrizione}}</p>
                    <q-badge color="green" class="q-mr-lg q-ml-lg">{{ personaggio.progressivo }}</q-badge>
                    <q-badge color="secondary" class="q-mr-lg">{{ personaggio.allineamento }}</q-badge>
                    <q-badge color="red">{{ personaggio.tipologia }}</q-badge>
                </q-card-section>
            </q-card>
        </q-expansion-item>
    </div>
    <!--    </q-page>-->
</template>

<style>
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'Personaggio',
        data() {
            return {
                left: false,
                counter: 0,
                lista: [1, 2, 3],
                personaggi: []
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
            },

            getPersonaggi() {
                const path = 'http://f4f9acf0.ngrok.io/personaggi';
                axios.get(path)
                    .then((res) => {
                        this.personaggi = res.data.personaggi;
                    })
            }
        },
        beforeDestroy() {
            this.stopCounting()
        },
        created() {
            this.getPersonaggi();
        }
    }
</script>
