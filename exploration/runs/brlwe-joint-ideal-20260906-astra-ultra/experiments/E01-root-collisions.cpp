#include <array>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

// Coordinator allocation E01. Deterministic exact enumeration, n <= 16.
// An external timeout of 120 seconds includes compilation and execution.
int modpow(int a,int e,int q){int z=1;for(;e;e>>=1,a=a*a%q)if(e&1)z=z*a%q;return z;}
int main(){
 auto started=std::chrono::steady_clock::now();
 std::cout << "{\"seed\":null,\"precision\":\"exact uint64 counts\",\"cases\":[";
 bool first=true;
 for(auto nq: std::vector<std::array<int,2>>{{4,17},{8,17},{16,97}}){
  int n=nq[0],q=nq[1]; std::vector<int> roots;
  for(int x=0;x<q;x++)if(modpow(x,n,q)==q-1)roots.push_back(x);
  if((int)roots.size()!=n)return 2;
  std::array<std::array<int,16>,16> powers{};
  std::array<int,16> values{},digits{};
  for(int j=0;j<n;j++)for(int k=0;k<n;k++){
   powers[j][k]=modpow(roots[k],j,q);values[k]=(values[k]+q-powers[j][k])%q;
  }
  std::array<uint64_t,17> h1{},h2{},pow2{},pow6{};
  pow2[0]=pow6[0]=1;for(int k=1;k<=n;k++){pow2[k]=pow2[k-1]*2;pow6[k]=pow6[k-1]*6;}
  std::array<unsigned,2> masks{};std::array<uint64_t,2> b1{},b2{};
  for(int b=0;b<2;b++){int d=2<<b;if(d<=n){int a=modpow(roots[0],d,q);for(int k=0;k<n;k++)if(modpow(roots[k],d,q)==a)masks[b]|=1u<<k;}}
  uint64_t total=1;for(int i=0;i<n;i++)total*=3;
  int zeros=0;
  for(uint64_t t=0;t<total;t++){
   unsigned mask=0;int z=0;for(int k=0;k<n;k++)if(!values[k]){mask|=1u<<k;z++;}
   h1[z]+=pow2[zeros];h2[z]+=pow6[zeros];
   for(int b=0;b<2;b++)if(masks[b] && (mask&masks[b])==masks[b]){b1[b]+=pow2[zeros];b2[b]+=pow6[zeros];}
   if(t+1==total)break;
   for(int j=0;j<n;j++){
    int delta;
    if(digits[j]==0){digits[j]=1;zeros++;delta=1;}
    else if(digits[j]==1){digits[j]=2;zeros--;delta=1;}
    else {digits[j]=0;delta=-2;}
    for(int k=0;k<n;k++){
     int v=values[k]+delta*powers[j][k];if(v<0)v+=q;if(v<0)v+=q;if(v>=q)v-=q;values[k]=v;
    }
    if(delta==1)break;
   }
   if((t&1048575)==0 && std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>110)return 3;
  }
  if(!first)std::cout<<",";first=false;
  std::cout<<"{\"n\":"<<n<<",\"q\":"<<q<<",\"enumerated\":"<<total<<",\"roots\":[";
  for(int k=0;k<n;k++){if(k)std::cout<<",";std::cout<<roots[k];}
  std::cout<<"],\"hist_beta1\":[";for(int k=0;k<=n;k++){if(k)std::cout<<",";std::cout<<h1[k];}
  std::cout<<"],\"hist_beta_half\":[";for(int k=0;k<=n;k++){if(k)std::cout<<",";std::cout<<h2[k];}
  std::cout<<"],\"binomial_masks\":["<<masks[0]<<","<<masks[1]<<"],\"binomial_beta1\":["<<b1[0]<<","<<b1[1]<<"],\"binomial_beta_half\":["<<b2[0]<<","<<b2[1]<<"]}";
 }
 std::cout<<"],\"runtime_seconds\":"<<std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()<<"}\n";
}
