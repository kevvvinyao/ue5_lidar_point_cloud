// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "RWer.generated.h"

/**
 * 
 */
UCLASS()
class LIDARPROJECT_API URWer : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

	UFUNCTION(BlueprintCallable)
	static FString ReadTxt(FString Filename);

	UFUNCTION(BlueprintCallable)
	static bool WriteTxt(FString content, FString Filename);

	
};
