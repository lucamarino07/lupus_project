import Vue from 'vue'

import './styles/quasar.styl'
// import lang from 'quasar/lang/(it-IT).js'
import '@quasar/extras/material-icons/material-icons.css'
import {
    Quasar,
    QLayout,
    QHeader,
    QDrawer,
    QPageContainer,
    QPage,
    QToolbar,
    QToolbarTitle,
    QBtn,
    QIcon,
    QList,
    QItem,
    QItemSection,
    QItemLabel,
    QTab,
    QTabs,
    QRouteTab,
    QAvatar,
    QExpansionItem,
    QCard,
    QCardSection,
    QBadge
} from 'quasar'

Vue.use(Quasar, {
    config: {},
    components: {
        QLayout,
        QHeader,
        QDrawer,
        QPageContainer,
        QPage,
        QToolbar,
        QToolbarTitle,
        QBtn,
        QIcon,
        QList,
        QItem,
        QItemSection,
        QItemLabel,
        QTab,
        QTabs,
        QRouteTab,
        QAvatar,
        QExpansionItem,
        QCard,
        QCardSection,
        QBadge
    },
    directives: {},
    plugins: {},
    // lang: lang
})