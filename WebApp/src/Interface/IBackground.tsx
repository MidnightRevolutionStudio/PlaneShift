import { IAbility } from "./IAbility";

export interface IBackground{
    name: string;
    startingProficiencies:string[];
    abilities:IAbility[];
}