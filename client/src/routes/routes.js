import { lazy } from 'react';

const Home = lazy(() => import('../pages/Home'));
const About = lazy(() => import('../pages/About'));

const PublicRoutes = [
    { path: '/', component: Home },
    { path: '/about', component: About },
];

export { PublicRoutes };