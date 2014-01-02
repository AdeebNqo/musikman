/*

Copyright 2013 Zola Mahlaza (Adeeb Nqo) <adeebnqo@gmail.com>
For license info, see LICENSE

*/
#include "../include/metadata.hpp"
#include<iostream>
#include<algorithm>
namespace music_man{

	metadata::metadata(char* path){		
		std::cout << "metadata created" << std::endl;
		infile = new std::ifstream(path);
		char* tmp = new char[128];
		while(!infile->eof()){
			infile->read(tmp,128);
		}
		std::reverse(&tmp[0], &tmp[127]);	
		
		//reading the title
		title = new char[30];
		int j=0;
		for (int i=3; i<34; ++i, ++j){
			title[j] = tmp[34-i];
		}
	};
	metadata::~metadata(){
		delete[] title;
		delete[] artist;
		delete[] album;
		delete infile;
	};
	char* metadata::get_artist(){
		return artist;
	};
	char* metadata::get_album(){
		return album;
	};
}
