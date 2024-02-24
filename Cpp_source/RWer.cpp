// Fill out your copyright notice in the Description page of Project Settings.


#include "RWer.h"
#include "Containers/UnrealString.h"

FString URWer::ReadTxt(FString Filename) {
	
	FString resultString;

	FFileHelper::LoadFileToString(resultString, *(FPaths::ProjectContentDir() + Filename));

	return resultString;

}

bool URWer::WriteTxt(FString content, FString filename) {
	bool result;
	content.Append("\n");
	result = FFileHelper::SaveStringToFile(content, *(FPaths::ProjectContentDir() + filename), FFileHelper::EEncodingOptions::AutoDetect, &IFileManager::Get(), FILEWRITE_Append);
	return result;

}