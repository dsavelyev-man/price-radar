"use client";

import Image from "next/image";
import { Header } from "./common/header";
import {HeroUIProvider} from "@heroui/react"

export default function Home() {
  return (
    <HeroUIProvider>
          <Header/>
    </HeroUIProvider>
    
  );
}
