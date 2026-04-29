<template>
    <v-container class="gallery">
        <v-row>
            <v-col cols="12">
                <v-bottom-navigation :value="pixelMode" color="primary">
                    <v-btn @click="pixelMode = 0">
                        <span>8x8 Pixel</span>
                        <v-icon>mdi-grid</v-icon>
                    </v-btn>
                    <v-btn @click="pixelMode = 1">
                        <span>8x32 Pixel</span>
                        <v-icon>mdi-grid</v-icon>
                    </v-btn>
                </v-bottom-navigation>
            </v-col>
        </v-row>
        <v-row v-if="pixelMode == 0">
            <v-col cols="12" lg="4" offset-lg="2">
                <v-card class="pa-3" elevation="4">
                    <Art :colors="colors" pixelCount="64" :func="onclick" />
                    <p></p>
                    <v-textarea filled outlined v-model="array8x8String" rows="5" hide-details readonly label="Код массива 8x8"></v-textarea>
                </v-card>
            </v-col>
            <v-col cols="12" lg="4">
                <v-card class="pa-3" elevation="4">
                    <v-color-picker v-model="colors" mode="hexa" show-swatches swatches-max-height="280"></v-color-picker>
                </v-card>
            </v-col>
        </v-row>
        <v-row v-if="pixelMode == 1">
            <v-col cols="12" lg="8">
                <v-card class="pa-3" elevation="4">
                    <Art :colors="colors" pixelCount="256" :func="onclick" />
                    <p></p>
                    <v-textarea filled outlined v-model="array8x32String" rows="9" hide-details readonly label="Код массива 8x32"></v-textarea>
                </v-card>
            </v-col>
            <v-col cols="12" lg="4">
                <v-card class="pa-3" elevation="4">
                    <v-color-picker v-model="colors" mode="hexa" show-swatches swatches-max-height="270"></v-color-picker>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import Art from './components/Art.vue';

export default {
    components: { Art },
    data() {
        return {
            colors: '#F44336',
            pixelMode: 0,
            active8x8Background: {},
            active8x32Background: {},
            array8x8String: '',
            array8x32String: '',
        };
    },
    methods: {
        onclick(id, color) {
            const hexColor = color.replace('#', '');
            if (this.pixelMode == 0) {
                this.active8x8Background[id] = hexColor;
                this.array8x8String = this.generateArray(this.active8x8Background, 64);
            } else {
                this.active8x32Background[id] = hexColor;
                this.array8x32String = this.generateArray(this.active8x32Background, 256);
            }
        },
        generateArray(storage, count) {
            let res = '[';
            for (let i = 0; i < count; i++) {
                const hex = storage[i] || '000000';
                res += this.rgb888ToRgb565(this.hexToRgb(hex)) + (i === count - 1 ? '' : ',');
            }
            return res + ']';
        },
        rgb888ToRgb565(rgb) {
            return ((rgb.r & 0xf8) << 8) + ((rgb.g & 0xfc) << 3) + (rgb.b >> 3);
        },
        hexToRgb(hex) {
            const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
            return result ? { r: parseInt(result[1], 16), g: parseInt(result[2], 16), b: parseInt(result[3], 16) } : { r:0, g:0, b:0 };
        }
    }
};
</script>
