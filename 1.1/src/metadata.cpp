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
		
		for (int i=0; i<128; ++i){
			std::cout << tmp[i];
		}	
	
		artist = new char[10];
		album = new char[10];
	};
	metadata::~metadata(){
		delete[] artist;
		delete[] album;
		delete infile;
	};
	char* metadata::get_artist(){
		char * hello = new char[6];		
		return hello;
	};
	char* metadata::get_album(){
		char * world = new char[6];
		return world;
	};
}
