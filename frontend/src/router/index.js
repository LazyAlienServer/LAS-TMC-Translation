import {
    createRouter,
    createWebHistory,
} from 'vue-router'
import routes from './routes'
import {globalAfterEach, globalBeforeEach} from './guards';


const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach(globalBeforeEach)
router.afterEach(globalAfterEach)

export default router
