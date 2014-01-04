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
		//std::reverse(&tmp[0], &tmp[127]);
		int tag_pos = 0;		
		for (int i=0; i<126; ++i){
			char t = tmp[i];
			char a = tmp[i+1];
			char g = tmp[i+2];
			if (t=='T' && a=='A' && g=='G'){
				tag_pos = i+3;
				break;
			}
		}
		/*
		
		Try reading the rest of the tag
		
		*/
		try{
			//reading title
			title = new char[30];
			for (int index=0; index<30; ++index,++tag_pos){
				title[index] = tmp[tag_pos];
			}
			//reading artist
			artist = new char[30];
			for (int index=0; index<30; ++tag_pos){
				artist[index] = tmp[tag_pos];
				std::cout << tmp[tag_pos];
			}
			std::cout << std::endl;
		}catch(std::exception e){
			std::cout << e.what() << std::endl;
		}
	};
	metadata::~metadata(){
		delete[] title;
		delete[] artist;
		//delete[] album;*/
		delete infile;
	};
	char* metadata::get_artist(){
		return artist;
	};
	char* metadata::get_album(){
		return album;
	};
}
