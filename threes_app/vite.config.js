import { defineConfig } from "vite";
import reactRefresh from "@vitejs/plugin-react-refresh";

// https://vitejs.dev/config/
export default defineConfig({
    build: { manifest: true },
    base: process.env === "production" ? "/static/" : "/",
    root: "./templates/threes_app/threes",
    plugins: [reactRefresh()],
});