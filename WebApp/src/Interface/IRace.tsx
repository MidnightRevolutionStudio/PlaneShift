import { Attribute } from "Class/Attribute";

export interface IRace {
    name: string;
    speed: number;
    attributeMods: Attribute[];
    alignment: string;
    size: string;
}